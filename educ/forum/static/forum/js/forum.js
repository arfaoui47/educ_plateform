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

    $scope.loadStudent = function(){
      $http.get('/api-auth/student/').then(function(response){
        $scope.students = response.data;
        return response.data;
      });
     };

    $scope.loadProfessor = function(){
      $http.get('/api-auth/professor/').then(function(response){
        $scope.professors = response.data;
        return response.data;
      });
     };


    $scope.loadPost();
    $scope.loadComment();
    $scope.loadStudent();
    $scope.loadProfessor();
    $scope.currentPost = {};
    $scope.currentComment = {};
    $scope.currentStudent = {};
    //$scope.errors = {};

    $scope.savePost = function(user_id){
        $scope.currentPost.student = user_id; // the user_id (temporally)
        ModelUtils.save('/api-auth/post/', $scope.currentPost).then(function(){
            $scope.loadPost();
            $scope.currentPost = {};
        });
    };
    $scope.delPost = function(post, user_id){
        if(post.student == user_id) { //test for the user_id (temporally)
            ModelUtils.del('/api-auth/post/', post).then(function () {
                $scope.loadPost();
            });
        }
    };

    $scope.saveComment = function(post, user_id){
        $scope.currentComment.user = user_id;
        $scope.currentComment.forumpost = post.id;
        $scope.currentComment.contents = $scope.currentComment.contents[post.id];
        ModelUtils.save('/api-auth/comment/', $scope.currentComment).then(function(){
            $scope.loadComment();
            $scope.currentComment = {};
        });
    };

    $scope.updateComment = function(post, comment, user_id){
        if(comment.user == user_id) {
            comment.contents = $scope.currentComment.contents[comment.id];
            ModelUtils.save('/api-auth/comment/', comment).then(function () {
                $scope.loadComment();
                $scope.currentComment = {};
            });
        }
    };
    $scope.delComment = function(comment, user_id){
        if(comment.user == user_id){
            ModelUtils.del('/api-auth/comment/', comment).then(function () {
                $scope.loadComment();
            });
        }
    };

    $scope.solve=function(post, user_id){
        if(post.student == user_id){
            post.statment = 1;
            ModelUtils.save('/api-auth/post/', post).then(function () {
                $scope.loadPost();
            });
        }
    }

    $scope.notsolved=function(post){
        if(post.statment == 0){
            return 1;
        }
        else{
            return 0;
        }
    }

    $scope.solved=function(post){
        if(post.statment == 0){
            return 0;
        }
        else{
            return 1;
        }
    }

    $scope.upprovalup=function(post, user_id){
        if(post.student != user_id){
            post.approval++;
            ModelUtils.save('/api-auth/post/', post).then(function () {
                $scope.loadPost();
            });
        }
    }

    $scope.upprovaldown=function(post, user_id){
        if(post.student != user_id){
            post.approval--;
            ModelUtils.save('/api-auth/post/', post).then(function () {
                $scope.loadPost();
            });
        }
    }
});
