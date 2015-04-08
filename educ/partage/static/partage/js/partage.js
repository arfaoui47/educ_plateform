angular
    .module('partage', ['angularFileUpload'])
    .controller('AppController', function($scope, FileUploader) {
        $scope.uploader = new FileUploader();
        url:upload;
    });
