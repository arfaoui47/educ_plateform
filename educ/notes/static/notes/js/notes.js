educ.controller('NotesCtrl', function PostCtrl($scope, $log, $http, ModelUtils){

    $scope.loadNotes = function(){
      $http.get('/api-auth/note/').then(function(response){
        $scope.notes = response.data;
        return response.data;
      });
     };

    $scope.loadClassroom = function(){
      $http.get('/api-auth/classroom/').then(function(response){
        $scope.classrooms = response.data;
        return response.data;
      });
     };

    $scope.loadSubject = function(){
      $http.get('/api-auth/subject/').then(function(response){
        $scope.subjects = response.data;
        return response.data;
      });
     };

    $scope.loadStudent = function(){
      $http.get('/api-auth/student/').then(function(response){
        $scope.students = response.data;
        return response.data;
      });
     };

    $scope.loadNotes();
    $scope.loadClassroom();
    $scope.loadStudent();
    $scope.loadSubject();
    $scope.currentNotes = {};

    $scope.saveNotes = function(subject_id, user_id){
        var Notes = $scope.currentNotes[subject_id];
        Notes = Notes["note"];
        var key;
        for(key in Notes){
            var Note = {};
            Note.professor = user_id;
            Note.student = parseInt(key);
            Note.note = parseInt(Notes[key]);
            ModelUtils.save('/api-auth/note/', Note).then(function () {
                Note = {};
            });
        }
        $scope.loadNotes();
        $scope.currentNotes[subject_id] = {};
    };


    $scope.updateNotes = function(notes, user_id){
        //if(comment.user == user_id) {
            //comment.contents = $scope.currentComment.contents[comment.id];
            ModelUtils.save('/api-auth/notes/', notes).then(function () {
                $scope.loadNotes();
                $scope.currentNotes = {};
            });
        //}
    };

});
