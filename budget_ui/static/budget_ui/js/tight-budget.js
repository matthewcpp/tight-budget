/// <reference path="typings/backbone-relational/backbone-relational.d.ts"/>
/// <reference path="typings/jquery/jquery.d.ts"/>
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    __.prototype = b.prototype;
    d.prototype = new __();
};
var TightBudget;
(function (TightBudget) {
    var Budget = (function (_super) {
        __extends(Budget, _super);
        function Budget(options) {
            _super.call(this, options);
            this.relations = [
                {
                    type: Backbone.HasMany,
                    key: 'categories',
                    relatedModel: 'TightBudget.Category',
                    includeInJSON: true,
                    collectionType: 'TightBudget.CategoryCollection',
                    reverseRelation: {
                        key: 'budget'
                    }
                }
            ];
        }
        return Budget;
    })(Backbone.RelationalModel);
    TightBudget.Budget = Budget;
    var BudgetCollection = (function (_super) {
        __extends(BudgetCollection, _super);
        function BudgetCollection() {
            _super.apply(this, arguments);
            this.url = '/api/budgets/';
            this.model = Budget;
        }
        return BudgetCollection;
    })(Backbone.Collection);
    TightBudget.BudgetCollection = BudgetCollection;
    var BudgetView = (function (_super) {
        __extends(BudgetView, _super);
        function BudgetView(options) {
            _super.call(this, options);
        }
        BudgetView.prototype.render = function () {
            console.log(this.model.get("name"));
            this.$el.html(this.model.get("name"));
            return this;
        };
        BudgetView.prototype.initialize = function () {
            this.listenTo(this.model, "change", this.render);
        };
        return BudgetView;
    })(Backbone.View);
    TightBudget.BudgetView = BudgetView;
})(TightBudget || (TightBudget = {}));
/// <reference path="typings/jquery/jquery.d.ts"/>
/// <reference path="Budget.ts"/>
var TightBudget;
(function (TightBudget) {
    var Application = (function () {
        function Application(data) {
            this._budgets = new TightBudget.BudgetCollection();
            this._budgetViews = [];
            this._setupInitialData(data);
        }
        Application.prototype._setupInitialData = function (data) {
            if (data.initialBudget) {
                this._budgets.reset([data.initialBudget]);
                this._budgetViews.push(new TightBudget.BudgetView({
                    model: this._budgets.at(0),
                    el: document.getElementById("recent-budget")
                }));
            }
        };
        Application.prototype.start = function () {
            for (var i = 0; i < this._budgetViews.length; i++) {
                this._budgetViews[i].render();
            }
        };
        return Application;
    })();
    TightBudget.Application = Application;
})(TightBudget || (TightBudget = {}));
var TightBudget;
(function (TightBudget) {
    var Category = (function (_super) {
        __extends(Category, _super);
        function Category() {
            _super.apply(this, arguments);
        }
        return Category;
    })(Backbone.RelationalModel);
    TightBudget.Category = Category;
    var CategoryCollection = (function (_super) {
        __extends(CategoryCollection, _super);
        function CategoryCollection() {
            _super.apply(this, arguments);
            this.url = '/api/categories/';
            this.model = Category;
        }
        return CategoryCollection;
    })(Backbone.Collection);
    TightBudget.CategoryCollection = CategoryCollection;
})(TightBudget || (TightBudget = {}));
