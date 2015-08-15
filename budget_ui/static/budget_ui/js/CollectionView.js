if (!window.TightBudget) window.TightBudget = {}

TightBudget.CollectionView = function(options){
	this._options = options;
	this._collectionViews = [];
	
	this.el = document.createElement(this._options.tagName);
	this.el.classList.add(this._options.className);
	this.$el = $(this.el);
	
	this._createInitialViews();
}

TightBudget.CollectionView.prototype.getCollection = function(){
	return this._options.collection;
}

TightBudget.CollectionView.prototype.render = function(){
	for (var i = 0; i < this._collectionViews.length; i++){
		this._collectionViews[i].render();
	}
}

TightBudget.CollectionView.prototype._createInitialViews = function(){
	var viewClass = this._options.viewClass;
	var collection = this.getCollection();
	
	var _this = this;
	collection.each(function(model){
		var view = new viewClass({
			model: model
		});
		
		view.render();
		
		_this.$el.append(view.el);
		_this._collectionViews.push(view);
	});
}