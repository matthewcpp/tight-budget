if (!window.TightBudget) window.TightBudget = {}

TightBudget.Category = Backbone.Model.extend({
	urlRoot: "api/categories"
});

TightBudget.CategoryCollection = Backbone.Collection.extend({
	url: "api/categories",
	model: TightBudget.Category
});

TightBudget.CategoryView = Backbone.View.extend({
	tagName: "div",
	className: "category-item",
	
	initialize: function(){
		this.listenTo(this.model, "change", this.render);
	},
	
	render: function(){
		if (!TightBudget.CategoryView._template) TightBudget.CategoryView._template = _.template($("#category-view-template").html(), {variable: "category"});
		
		this.$el.html(TightBudget.CategoryView._template(this.model.toJSON()));
		return this;
	}
});

TightBudget.CategoryInfo = function(collection, view){
	this.collection = collection;
	this.view = view;
} 
