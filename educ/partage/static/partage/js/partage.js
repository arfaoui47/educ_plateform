educ.controller('ParCtrl', function ($scope,$http) {
      $scope.loadfile = function(){
      $http.get('/api-auth/uploads/').then(function(response){
        $scope.fichs = response.data;
        return response.data;
      });
     };
    $scope.loadfile();
    $scope.loadsubject = function(){
      $http.get('/api-auth/subject/').then(function(response){
        $scope.subjs = response.data;
        return response.data;
      });
     };
    $scope.loadsubject();
});