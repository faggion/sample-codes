var MyBlogApp = angular.module('MyBlogApp', ['ngRoute', 'ngSanitize', 'myBlogControllers']);
var myBlogControllers = angular.module('myBlogControllers', []);

myBlogControllers.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('||');
    $interpolateProvider.endSymbol('||');
});

myBlogControllers.config(['$routeProvider',
                  function($routeProvider) {
                      $routeProvider.
                          when('/contents', {
                              templateUrl: '/static/templates/content_list.html',
                              controller: 'ContentListCtrl'
                          }).
                          when('/new_content', {
                              templateUrl: '/static/templates/content_new.html',
                              controller: 'ContentNewCtrl'
                          }).
                          when('/contents/:content_id', {
                              templateUrl: '/static/templates/content_detail.html',
                              controller: 'ContentDetailCtrl'
                          }).
                          otherwise({
                              redirectTo: '/contents'
                          });
                  }]);
     
myBlogControllers.controller('ContentNewCtrl',
                             ['$scope', '$http',
                              function ($scope, $http) {
                                  console.debug('new content');
                              }]);

myBlogControllers.controller('ContentListCtrl',
                             ['$scope', '$http',
                              function ($scope, $http) {
                                  $http.get('/api/v1/content?rg=large').success(function(data) {
                                      $scope.contents = data;
                                  }).error(function(data){ console.debug('error'); });
                              }]);

myBlogControllers.controller('ContentSaveCtrl',
                             ['$scope', '$http',
                              function ($scope, $http) {
                                  $scope.data = {
                                      published_at: (new Date()).toISOString(),
                                  };
                                 
                                  $scope.submit = function(){
                                      $scope.data.content = $('#preview').html();
                                      console.debug($scope.data);
                                      $http.put('/api/v1/content', $scope.data).success(
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
     
myBlogControllers.controller('ContentDetailCtrl',
                             ['$scope', '$routeParams', '$http',
                              function($scope, $routeParams, $http) {
                                  $http.get('/api/v1/content/' + $routeParams.content_id).success(
                                      function(data) {
                                          $scope.content_id = data.id;
                                          $scope.content_name = data.name;
                                      }
                                  )
                              }]);