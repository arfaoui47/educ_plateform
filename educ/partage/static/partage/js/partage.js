educ.controller('ParCtrl', function ($scope,$http,ModalService) {
    $scope.loadfile = function () {
        $http.get('/api-auth/uploads/').then(function (response) {
            $scope.fichs = response.data;
            return response.data;
        });
    };
    $scope.loadfile();
    $scope.loadsubject = function () {
        $http.get('/api-auth/subject/').then(function (response) {
            $scope.subjs = response.data;
            return response.data;
        });
    };
    $scope.loadsubject();

    $scope.istd = function(fich){
        if (fich.type == "td"){
            return 1;
        }
        else
            return 0;
    };

    $scope.istp = function(fich){
        if (fich.type == "tp"){
            return 1;
        }
        else
            return 0;
    };

    $scope.islesson = function(fich){
        if (fich.type == "lesson"){
            return 1;
        }
        else
            return 0;
    };

    $scope.iselse = function(fich){
        if ((fich.type != "td")&&(fich.type != "tp")&&(fich.type != "lesson")){
            return 1;
        }
        else
            return 0;
    };

    //modal
  $scope.show = function(type, subj, fichs) {
        ModalService.showModal({
            templateUrl: 'modal.html',
            controller: "ModalController",
            inputs: {
                type: type,
                subj: subj,
                fichs: fichs
            }
        }).then(function(modal) {
            modal.element.modal();
            modal.close.then(function() {
                console.log("closed");
            });
        });
    };

});

educ.controller('ModalController', function($scope, close, type, subj, fichs) {

 $scope.type = type;
 $scope.subj = subj;
 $scope.fichs = fichs;
 $scope.close = function(result) {
 	close(result, 500);
 };

});