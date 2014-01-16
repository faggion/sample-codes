var tanarkyApp = angular.module('tanarkyApp', ['ngResource']);
     
tanarkyApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('||');
    $interpolateProvider.endSymbol('||');
});

tanarkyApp.controller('userCtrl', function($scope, $resource){
    var User = $resource('/api/v1/user/:id', {id:'@id'}, {put: {method: 'PUT'}});

    var users = User.query(function() {
        console.debug(users[0]);
        var u = users[0];
        u.name = 'foo';
        u.$put();
    });

    var u1 = User.get({'id':133});
    var u2 = User.put({'id':133, 'name':'foo', 'age':23});
});