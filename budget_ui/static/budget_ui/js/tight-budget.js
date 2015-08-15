/// <reference path="typings/backbone-relational/backbone-relational.d.ts"/>
/// <reference path="typings/jquery/jquery.d.ts"/>
var __extends = this.__extends || function (d, b) {
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
                    reverseRelation: {
                        key: 'budget'
                    }
                }
            ];
            this.initializeRelations(this.relations);
        }
        Budget.prototype.getCategories = function () {
            return this.get("categories");
        };
        return Budget;
    })(Backbone.RelationalModel);
    TightBudget.Budget = Budget;
    var BudgetCollection = (function (_super) {
        __extends(BudgetCollection, _super);
        function BudgetCollection(options) {
            _super.call(this, options);
            this.url = '/api/budgets/';
            this.model = TightBudget.Budget;
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
            this.$el.html(this.model.get("name"));
            return this;
        };
        BudgetView.prototype.initialize = function () {
            this.listenTo(this.model, "change", this.render);
        };
        BudgetView.setupTemplate = function () {
            if (BudgetView._template == null) {
                BudgetView._template = _.template("<h3> {{ name }} </h3>");
            }
        };
        return BudgetView;
    })(Backbone.View);
    TightBudget.BudgetView = BudgetView;
})(TightBudget || (TightBudget = {}));
TightBudget.Budget.setup();
/// <reference path="typings/jquery/jquery.d.ts"/>
/// <reference path="Budget.ts"/>
var TightBudget;
(function (TightBudget) {
    var Application = (function () {
        function Application(data) {
            this._router = new TightBudget.Router(this);
        }
        /*
        private _setupInitialData(data: InitialApplicationData){
            if (data.initialBudget){
                this._budgets.reset([data.initialBudget]);
                
                this._budgetViews.push(new BudgetView({
                    model: this._budgets.at(0),
                    el: document.getElementById("recent-budget")
                }));
            }
        }
        */
        Application.prototype.start = function () {
            Backbone.history.start();
        };
        return Application;
    })();
    TightBudget.Application = Application;
})(TightBudget || (TightBudget = {}));
var TightBudget;
(function (TightBudget) {
    var Category = (function (_super) {
        __extends(Category, _super);
        function Category(options) {
            _super.call(this, options);
        }
        return Category;
    })(Backbone.RelationalModel);
    TightBudget.Category = Category;
    var CategoryCollection = (function (_super) {
        __extends(CategoryCollection, _super);
        function CategoryCollection(options) {
            _super.call(this, options);
            this.url = '/api/categories/';
            this.model = TightBudget.Category;
        }
        return CategoryCollection;
    })(Backbone.Collection);
    TightBudget.CategoryCollection = CategoryCollection;
    var CategoryView = (function (_super) {
        __extends(CategoryView, _super);
        function CategoryView(options) {
            _super.call(this, options);
        }
        CategoryView.prototype.render = function () {
            this.$el.html(this.model.get("name"));
            return this;
        };
        CategoryView.prototype.initialize = function () {
            this.listenTo(this.model, "change", this.render);
        };
        return CategoryView;
    })(Backbone.View);
    TightBudget.CategoryView = CategoryView;
})(TightBudget || (TightBudget = {}));
TightBudget.Category.setup();
/// <reference path="typings/backbone/backbone.d.ts"/>
var TightBudget;
(function (TightBudget) {
    var Router = (function (_super) {
        __extends(Router, _super);
        function Router(application, options) {
            _super.call(this, options);
            this.routes = { "": "show_main_view" };
            this._application = application;
        }
        return Router;
    })(Backbone.Router);
    TightBudget.Router = Router;
})(TightBudget || (TightBudget = {}));
