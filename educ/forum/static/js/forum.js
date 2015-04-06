educ.controller('PostCtrl', function PostCtrl($scope, $log, $http, ModelUtils){

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
    $scope.currentStudent = {};
    //$scope.errors = {};

    $scope.savePost = function(){
        $scope.currentPost.student = 1; // the user_id (temporally)
        ModelUtils.save('/api-auth/post/', $scope.currentPost).then(function(){
            $scope.loadPost();
            $scope.currentPost = {};
        });
    };
    $scope.delPost = function(post){
        if(post.student == 1) { //test for the user_id (temporally)
            ModelUtils.del('/api-auth/post/', post).then(function () {
                $scope.loadPost();
            });
        }
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

    $scope.updateComment = function(post, comment){
        $scope.currentComment.user = 1;
        $scope.currentComment.forumpost = post.id;
        $scope.currentComment.id = comment.id;
        $scope.currentComment.contents = $scope.currentComment.contents[comment.id];
        ModelUtils.save('/api-auth/comment/', $scope.currentComment).then(function(){
            $scope.loadComment();
            $scope.currentComment = {};
        });
    };
    $scope.delComment = function(comment){
        ModelUtils.del('/api-auth/comment/',comment).then(function(){
           $scope.loadComment();
        });
    };
});
