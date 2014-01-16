function BlogCtrl($scope) {
    
    $scope.addArticle = function() {
        console.debug('called add article');
        $scope.$apply(function(){ $http.get('/').success(function(d,s,h,c){}); });
        //$scope.todos.push({text:$scope.todoText, done:false});
        //$scope.todoText = '';
        //$scope.$apply(function(){
        //    $http({
        //        method: "POST",
        //        url: "/",
        //        data: { title: $scope.articleTitle }
        //    }).
        //        success(function(data, status, headers, config){ console.debug(data); }).
        //        error(function(data, status, headers, config){ console.debug('error'); });
        //});
    };
    
}
