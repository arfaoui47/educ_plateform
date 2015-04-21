educ.controller('NotificationCtrl', function NotificationCtrl($scope, $log, $http, ModelUtils){


    $scope.loadNotification = function(){
      $http.get('/api-auth/notification/').then(function(response){
        $scope.notifications = response.data;
        return response.data;
      });
     };


    $scope.loadNotification();

    //add new notification
    /*$scope.saveNotification = function(post){
        notification =
        ModelUtils.save('/api-auth/notification/', notification.then(function(){
            $scope.loadNotification();
        });
    };*/

    //update statment of notification
    $scope.updateNotification = function(notification){
        notification.statement = true;
        ModelUtils.save('/api-auth/notification/', notification).then(function () {
            $scope.loadNotification();
        });
    };

    //del notification
    /*$scope.delNotification = function(notification){
        ModelUtils.del('/api-auth/notification/', notification).then(function () {
            $scope.loadNotification();
        });
    };*/

    $scope.read = function(notification){
        if(notification.statement == true){
            return 1;
        }
        else{
            return 0;
        }
    };

    $scope.notread = function(notification){
        if(notification.statement == true){
            return 0;
        }
        else{
            return 1;
        }
    };

    $scope.onenotread = function(notifications, user_id){
        var key;
        for(key in notifications) {
            if ((notifications[key].user == user_id) && (notifications[key].statement == false)) {
                return 1;
            }
        }
        return 0;
    };

    $scope.allread = function(notifications, user_id){
        var key;
        for(key in notifications) {
            if ((notifications[key].user == user_id) && (notifications[key].statement == false)) {
                return 0;
            }
        }
        return 1;
    };
});
