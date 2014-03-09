var APP = angular.module('MyBlogApp', ['ngRoute', 'ngSanitize', 'myBlogControllers']);
var CTR = angular.module('myBlogControllers', []);

CTR.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('||');
    $interpolateProvider.endSymbol('||');
});

CTR.config(['$routeProvider',
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
                    when('/tags', {
                        templateUrl: '/static/templates/tag_list.html',
                    }).
                    when('/new_tag', {
                        templateUrl: '/static/templates/tag_new.html',
                        controller: 'TagNewCtrl'
                    }).
                    otherwise({
                        redirectTo: '/contents'
                    });
            }]);

CTR.controller('ContentNewCtrl',
               ['$scope', '$http',
                function ($scope, $http) {                                  
                    console.debug('new content');
                }]);

CTR.controller('ContentListCtrl',
               ['$scope', '$http',
                function ($scope, $http) {
                    $http.get('/api/v1/content?rg=large').success(function(data) {
                        $scope.contents = data;
                    }).error(function(data){ console.debug('error'); });
                }]);


CTR.controller('ContentSaveCtrl',
               ['$scope', '$http',
                function ($scope, $http) {
                    $scope.data = {
                        "published": true,
                    };
                    
                    $scope.submit = function(){
                        $scope.data.content = $('#main_contents').html();
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
     
CTR.controller('ContentDetailCtrl',
               ['$scope', '$routeParams', '$http',
                function($scope, $routeParams, $http) {
                    $http.get('/api/v1/content/' + $routeParams.content_id).success(
                        function(data) {
                            $scope.content_id = data.id;
                            $scope.content_name = data.name;
                        }
                    )
                }]);

/*
 * Tag
 */
var API_TAG = '/api/v1/tag'
CTR.controller('TagListCtrl',
               ['$scope', '$http',
                function ($scope, $http) {
                    $http.get(API_TAG, {params:{rg:'large'}}).success(function(rsp) {
                        $scope.tags = rsp;
                    }).error(function(rsp){console.debug('error');});
                }]);

CTR.controller('TagSaveCtrl',
               ['$scope', '$http',
                function ($scope, $http) {
                    $scope.submit = function(){
                        if($scope.newTag.parentNum){
                            $scope.newTag.parentNum = parseInt($scope.newTag.parentNum);
                        }
                        else {
                            $scope.newTag.parentNum = undefined;
                        }
                        console.debug($scope.newTag);
                        console.debug($scope.tags);
                        $http.put(API_TAG, $scope.newTag).success(function(rsp) {
                            console.debug(rsp);
                            $scope.tags.push(rsp);
                        }).error(function(rsp){console.debug('error');});
                    };
                }]);

