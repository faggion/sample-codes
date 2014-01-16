function BlogCtrl($scope) {
    
    $scope.addArticle = function() {
        //$scope.todos.push({text:$scope.todoText, done:false});
        //$scope.todoText = '';
        $http({
            method: "POST",
            url: "http://localhost:5000/",
            data: { title: $scope.articleTitle }
        }).
            success(function(data, status, headers, config){ console.debug(data); }).
            error(function(data, status, headers, config){ console.debug('error'); })
    };
    
/*
    $scope.remaining = function() {
        var count = 0;
        angular.forEach($scope.todos, function(todo) {
            count += todo.done ? 0 : 1;
        });
        return count;
    };
    
    $scope.archive = function() {
        var oldTodos = $scope.todos;
        $scope.todos = [];
        angular.forEach(oldTodos, function(todo) {
            if (!todo.done) $scope.todos.push(todo);
        });
    };
*/
}
