//var MyBlogApp = angular.module('MyBlogApp', ['ngResource']);
//var MyBlogApp = angular.module('MyBlogApp', []);
var MyBlogApp = angular.module('MyBlogApp', ['ngRoute', 'myBlogControllers']);

MyBlogApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('||');
    $interpolateProvider.endSymbol('||');
});

MyBlogApp.config(['$routeProvider',
                  function($routeProvider) {
                      $routeProvider.
                          when('/articles', {
                              templateUrl: '/static/templates/articles.html',
                              controller: 'articlesCtrl'
                          }).
                          when('/articles/:articleId', {
                              templateUrl: '/static/templates/article_detail.html',
                              controller: 'articleDetailCtrl'
                          }).
                          otherwise({
                              redirectTo: '/articles'
                          });
                  }]);


/*
MyBlogApp.controller('articlesCtrl', function($scope, $resource){
    var Article = $resource('/api/article/:id', {id:'@id'});

    $scope.articles = Article.query(function() {
        console.debug($scope.articles);
    });

    //var a1 = Article.get({'id':133},
    //                     // success
    //                     function(){
    //                         console.debug(a1.method);
    //                         console.debug(a1.name);
    //                     });
    
});

MyBlogApp.controller('articlesCtrl', function($scope, $http){
    $http.get('/api/article').success(function(data){
        console.debug(data);
        $scope.articles = data;
    });
});

*/
