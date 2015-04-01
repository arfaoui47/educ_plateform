var forum = angular.module('forum',['ngCookies']);

forum.config(function($interpolateProvider) {
   $interpolateProvider.startSymbol('//');
   $interpolateProvider.endSymbol('//');
});

forum.run(function($rootScope, $log, $http, $cookies){
    $http.default.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
})


forum.factory('ModeUtils', function($http, $log){
   var ModeUtils = {
       get: function(url, id){
           $http.get(url + id + '/').then(function(response){response.data});
       },
       create: function(url, obj){
           return $http.post(url, obj).
               success(function(response, status, headers, config){
                   angular.extend(obj, reponse);
               }).
               error(function(response, status, headers, config){

               });
       },
       save: function(url, obj){
           if(angular.isDefined(obj.id)) {
               return $http.put(url + obj.id + '/', obj).
                   success(function (response, status, headers, config) {
                       angular.extend(obj, reponse);
                   }),
                   error(function (response, status, headers, config) {

                   });
           }else{
               return this.create(url, obj);
           }

       },
       del: function(url, obj){
           return $http.delete(url + obj.id + '/');
       }
   };
    return ModeUtils;


});
forum.controller('PostCtrl', function PostCtrl($scope, $log, $http, ModeUtils){

    $scope.initialize = function(data){
        $log.log('initialize', data);
        $scope.initData = data;

    };

    $scope.loadPost = function(){
        $scope.posts = $http.get('/api-auth/post/').then(function(response){
            return response.data;
        });
    };

    $scope.loadPost();
    $scope.currentPost = {};
    $scope.errors = {};

    $scope.savePost = function() {
        ModeUtils.save('/api-auth/post', $scope.currentPost, $scope.errors).then(function(){
            $scope.loadPost();
            $scope.currentPost = {};
        });
    };
    $scope.delPost = function(post) {
        ModeUtils.del('/api-auth/post',post).then(function(){
            $scope.loadPost();
        });
    };


});
