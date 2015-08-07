/// <reference path="typings/backbone-relational/backbone-relational.d.ts"/>
/// <reference path="typings/jquery/jquery.d.ts"/>

module TightBudget{	
	export class Budget extends Backbone.RelationalModel{
		relations = [
			{
				type: Backbone.HasMany, // Use the type, or the string 'HasOne' or 'HasMany'.
				key: 'categories',
				relatedModel: 'TightBudget.Category',
				includeInJSON: true,
				collectionType: 'TightBudget.CategoryCollection',
				reverseRelation: {
				    key: 'budget'
				}
			}
		];
	
		constructor(options?) {
	        super(options);
	    }
	}
	
	export class BudgetCollection extends Backbone.Collection<Budget>{
		url= '/api/budgets/'
		model = Budget;
	}
	
	export class BudgetView extends Backbone.View<Budget>{
		constructor(options?) {
	        super(options);
	    }
		
		render(): BudgetView{
			this.$el.html(this.model.get("name"));
			return this;
		}
		
		initialize (){
			this.listenTo(this.model, "change", this.render);
		}
	}
}
