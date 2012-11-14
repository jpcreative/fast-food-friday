'use strict';

var app = angular.module('fff', ['tastypieModule'])
    .config(function($routeProvider) { $routeProvider.
        when('/', {controller:HomeCrtl, templateUrl:'partials/home.html'}).
        when('/user', {controller:SiginInCtrl, templateUrl:'partials/sign-in.html'}).
        when('/no-connection', {templateUrl:'partials/no-connection.html'}).
        when('/list', {controller:ListCtrl, templateUrl:'partials/list.html'}).
        when('/add', {controller:CreateCtrl, templateUrl:'partials/add_option.html'}).
        otherwise({redirectTo:'/'});
    });
