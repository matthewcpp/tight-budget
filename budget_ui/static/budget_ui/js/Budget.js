if (!window.TightBudget) window.TightBudget = {}

TightBudget.Budget = Backbone.Model.extend({
	urlRoot: "api/budgets",
});

TightBudget.BudgetCollection = Backbone.Collection.extend({
	url: "api/budgets",
	model: TightBudget.Budget
});

TightBudget.BudgetView = Backbone.View.extend({
	initialize: function(){
		var _this = this;
		
		this.listenTo(this.model, "change", this.render);
	},
	
	events: {
		"click .new-transaction-button": "_onNewTransactionClick"
	},
	
	render: function(){
		if (!TightBudget.BudgetView._template) TightBudget.BudgetView._template = _.template($("#budget-view-template").html(), {variable: "budget"});
		
		this.$el.html(TightBudget.BudgetView._template(this.model.toJSON()));
		
		return this;
	},
	
	_onNewTransactionClick: function(){
		console.log("new transaction click");
	}
});

TightBudget.BudgetInfo = function(model, view){
	this.model = model;
	this.view = view;
} 