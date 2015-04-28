var educ = angular.module('educ',['ngCookies', 'angularModalService', 'ui.bootstrap']);

educ.config(function($interpolateProvider) {
   $interpolateProvider.startSymbol('//');
   $interpolateProvider.endSymbol('//');
});


educ.run(function($rootScope, $log, $http, $cookies){
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});


educ.factory('ModelUtils', function($http, $log){
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