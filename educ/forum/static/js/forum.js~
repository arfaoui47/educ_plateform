var forum = angular.module('forum',['ngCookies']);

forum.config(function($interpolateProvider) {
   $interpolateProvider.startSymbol('//');
   $interpolateProvider.endSymbol('//');
});

forum.run(function($rootScope, $log, $http, $cookies){
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});


forum.factory('ModelUtils', function($http, $log){
   var ModelUtils = {
       get: function(url, id){
           $http.get(url + id + '/').then(function(response){response.data});
       },
       create: function(url, obj){
           return $http.post(url, obj).
               success(function(response, status, headers, config){
                   angular.extend(obj, reponse);
               });
       },
       save: function(url, obj){
           if(angular.isDefined(obj.id)) {
               return $http.put(url + obj.id + '/', obj).
                   success(function (response, status, headers, config) {
                       angular.extend(obj, reponse);
                   });
           }else{
               return this.create(url, obj);
           }

       },
       del: function(url, obj){
           return $http.delete(url + obj.id + '/');
       }
   };
    return ModelUtils;

});

forum.controller('PostCtrl', function PostCtrl($scope, $log, $http, ModelUtils){

    $scope.initialize = function(data){
        $log.log('initialize', data);
        $scope.initData = data;

    };

    $scope.loadPost = function(){
      $http.get('/api-auth/post/').then(function(response){
        $scope.posts = response.data;
        return response.data;
      });
     };

    $scope.loadComment = function(){
      $http.get('/api-auth/comment/').then(function(response){
        $scope.comments = response.data;
        return response.data;
      });
     };

    $scope.loadPost();
    $scope.loadComment();
    $scope.currentPost = {};
    $scope.currentComment = {};
    //$scope.errors = {};

    $scope.savePost = function(){
        $scope.currentPost.student = 1;
        ModelUtils.save('/api-auth/post/', $scope.currentPost).then(function(){
            $scope.loadPost();
            $scope.currentPost = {};
        });
    };
    $scope.delPost = function(post){
        ModelUtils.del('/api-auth/post/',post).then(function(){
           $scope.loadPost();
        });
    };

    $scope.saveComment = function(post){
        $scope.currentComment.user = 1;
        $scope.currentComment.forumpost = post.id;
        $scope.currentComment.contents = $scope.currentComment.contents[post.id];
        ModelUtils.save('/api-auth/comment/', $scope.currentComment).then(function(){
            $scope.loadComment();
            $scope.currentComment = {};
        });
    };



});