if (!window.TightBudget) window.TightBudget = {}

TightBudget.Transaction = Backbone.Model.extend({
	
});

TightBudget.TransactionCollection = Backbone.Collection.extend({
	model: TightBudget.Transaction,
})

TightBudget.NewTransactionView = Backbone.View.extend({
	tagName: "div",
	className: "transaction-new",
	
	events: {
		"click .new-transaction-submit": "_onSubmitTransaction"
	},
	
	render: function(){
		if (!TightBudget.NewTransactionView._template) TightBudget.NewTransactionView._template = _.template($("#transaction-new-form").html(), {variable: "budget"});
		
		this.$el.html(TightBudget.NewTransactionView._template(this.model.toJSON()));
		
		return this;
	},
	
	_onSubmitTransaction: function(){
		
	}
});