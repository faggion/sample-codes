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
                                  $scope.submit = function(){
                                      console.debug($('#form_id').val());
                                      console.debug($('#form_title').val());

                                      var data = {title: $('#form_title').val(),
                                                  id: $('#form_id').val()};
                                      $http.post('/api/v1/content/'+ data.id, data).success(
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