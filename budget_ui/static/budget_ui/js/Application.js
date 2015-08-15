if (!window.TightBudget) window.TightBudget = {}

TightBudget.Application = Backbone.Router.extend({
	routes: {
		"": "showHomeScreen",
	},
	
	initialize: function (options){
		this._options = options;
		
		this._budgetCache = {};
		this._budgetCategoryCache = {};
		this._initialBudgetId = null;
		
		this._createInitialObjects();
	},
	
	start(){
		Backbone.history.start();
	},
	
	showHomeScreen: function(){
		console.log("showHomeScreen");
		
		var budgetInfo = this._budgetCache[this._initialBudgetId];
		budgetInfo.view.render();
		
		var categoryInfo = this._budgetCategoryCache[this._initialBudgetId];
		categoryInfo.view.render();
		
		
		var newTransactionView = new TightBudget.NewTransactionView({
			model: budgetInfo.model,
			el: document.getElementById("new-transaction")
		});
		
		newTransactionView.render();
		
		$("#recent-budget .category-list").append(categoryInfo.view.el);
	},
	
	_createInitialObjects(){
		var initialBudget = new TightBudget.Budget(this._options.initialData.budget);
		
		var initialBudgetId = initialBudget.get("id");
		
		var initialBudgetView = new TightBudget.BudgetView({
			model: initialBudget,
			el: document.getElementById("recent-budget")
		});
		
		this._budgetCache[initialBudgetId] = new TightBudget.BudgetInfo(initialBudget, initialBudgetView);
		
		var initialBudgetCategories = new TightBudget.BudgetCollection();
		initialBudgetCategories.reset(this._options.initialData.categories);
		
		
		var initialBudgetCategoriesView = new TightBudget.CollectionView({
			collection: initialBudgetCategories,
			viewClass: TightBudget.CategoryView,
			tagName: "div",
			className: "budget-category-items"
		});
		
		this._budgetCategoryCache[initialBudgetId] = new TightBudget.CategoryInfo(initialBudgetCategories, initialBudgetCategoriesView);
		
		this._initialBudgetId = initialBudgetId;
	}
});