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
                                  $scope.submit = function(){
                                      console.debug($('#form_id').val());
                                      console.debug($('#form_title').val());

                                      var data = {title: $('#form_title').val(),
                                                  id: $('#form_id').val()};
                                      $http.post('/api/article/'+ data.id, data).success(
                                          function(data){
                                              console.debug(data);
                                          }
                                      ).error(
                                          function(data){
                                              console.debug('ERROR');
                                              console.debug(data);
                                          }
                                      )
                                  };
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