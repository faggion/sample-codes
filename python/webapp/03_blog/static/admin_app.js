var MyBlogApp = angular.module('MyBlogApp', ['ngRoute', 'myBlogControllers']);

MyBlogApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('||');
    $interpolateProvider.endSymbol('||');
});

MyBlogApp.config(['$routeProvider',
                  function($routeProvider) {
                      $routeProvider.
                          when('/articles', {
                              templateUrl: '/static/templates/article_list.html',
                              controller: 'ArticleListCtrl'
                          }).
                          when('/articles/:article_id', {
                              templateUrl: '/static/templates/article_detail.html',
                              controller: 'ArticleDetailCtrl'
                          }).
                          otherwise({
                              redirectTo: '/articles'
                          });
                  }]);
