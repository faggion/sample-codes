var myBlogControllers = angular.module('myBlogControllers', []);
     
myBlogControllers.controller('ArticleListCtrl',
                             ['$scope', '$http',
                              function ($scope, $http) {
                                  $http.get('/api/article').success(function(data) {
                                      $scope.articles = data;
                                  }).error(function(data){ console.debug('error'); });
                              }]);

myBlogControllers.controller('ArticleNewCtrl',
                             ['$scope', '$http',
                              function ($scope, $http) {
                                  console.debug('new article');
                              }]);

myBlogControllers.controller('ArticleSaveCtrl',
                             ['$scope', '$http',
                              function ($scope, $http) {
                                  console.debug('saving article');
                                  $scope.submit = function(){ console.debug('yes, saved!'); };
                              }]);
     
myBlogControllers.controller('ArticleDetailCtrl',
                             ['$scope', '$routeParams', '$http',
                              function($scope, $routeParams, $http) {
                                  $http.get('/api/article/' + $routeParams.article_id).success(
                                      function(data) {
                                          $scope.article_id = data.id;
                                          $scope.article_name = data.name;
                                      }
                                  )
                              }]);