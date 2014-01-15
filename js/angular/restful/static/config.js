var tanarkyApp = angular.module('tanarkyApp', ['ngResource']);
     
tanarkyApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('||');
    $interpolateProvider.endSymbol('||');
});

tanarkyApp.controller('userCtrl', function($scope, $resource){
    var user = $resource('/api/v1/user');
    var u = user.get();
});