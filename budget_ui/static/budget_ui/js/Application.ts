/// <reference path="typings/jquery/jquery.d.ts"/>

/// <reference path="Budget.ts"/>

module TightBudget{	
	interface InitialApplicationData{
		initialBudget: Budget;
	}
	
	export class Application{
		private _budgets = new BudgetCollection();
		private _budgetViews: Array<BudgetView> = [];
		
		constructor (data: InitialApplicationData){
			this._setupInitialData(data);
		}
		
		private _setupInitialData(data: InitialApplicationData){
			if (data.initialBudget){
				this._budgets.reset([data.initialBudget]);
				
				this._budgetViews.push(new BudgetView({
					model: this._budgets.at(0),
					el: document.getElementById("recent-budget")
				}));
			}
		}
		
		public start(){
			for (var i =0; i < this._budgetViews.length; i++){
				this._budgetViews[i].render();
			}
		}
	}
}