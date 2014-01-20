var myBlogControllers = angular.module('myBlogControllers', []);
     
myBlogControllers.controller('ArticleListCtrl',
                             ['$scope', '$http',
                              function ($scope, $http) {
                                  $http.get('/api/article').success(function(data) {
                                      $scope.articles = data;
                                  }).error(function(data){ console.debug('error'); });
                              }]);
     
myBlogControllers.controller('ArticleDetailCtrl',
                             ['$scope', '$routeParams',
                              function($scope, $routeParams) {
                                  $scope.article_id = $routeParams.article_id;
                              }]);