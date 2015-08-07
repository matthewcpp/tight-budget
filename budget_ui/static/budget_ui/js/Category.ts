module TightBudget{
	export class Category extends Backbone.RelationalModel{
		
	}
	
	export class CategoryCollection extends Backbone.Collection<Category>{
		url= '/api/categories/'
		model = Category;
	}
}