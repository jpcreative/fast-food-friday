'use strict';

function getURLParameter(name, url) {
  return decodeURI((RegExp(name + '=' + '(.+?)(&|$)').exec(url) || [, null])[1]);
}

function checkConnection($location) {
  var online = navigator.onLine;

  if (online === false) {
    $location.path('/no-connection');
  }

  return online;
}

app.controller('MainAppCtrl', function($scope, $rootScope, $location, apiCall) {
  $rootScope.$on('event:auth-loginRequired', function() {
    $location.path('/');
  });

  $scope.twitterAvatar = apiCall.get({
    type: 'avatar',
    username: localStorage.getItem("username"),
    api_key: localStorage.getItem("apiKey"),
    user: localStorage.getItem("userID")
  });
});

app.controller('tabCtrl', function($scope, $location) {
    $scope.isActive = function(route) {
        return route === $location.path();
    }
});



function HomeCrtl($scope, $location) {
  
  //check for connecton 
  var online = navigator.onLine;

  //if connected attempt to login
  if (online === true) {
    $location.path('/user');

    //else show connection error
  } else {
    $location.path('/no-connection');
  }
};

function SiginInCtrl($scope, $location, apiCall) {
  $scope.twitterSignIn = function() {
    var theURL;

    if (typeof forge === "undefined") {
      theURL = 'http://192.168.91.96/auth/?username=artitudinale&api_key=0ee2e04b1e4e5ec3e60d436194d3b37b9a3c0f14&user=6';
      setLocalStorage(theURL);
      $location.path('/list');
    } else {
      forge.tabs.openWithOptions({
        url: 'http://192.168.91.96/accounts/twitter/login/',
        pattern: 'http://192.168.91.96/auth/*'
      }, function(data) {
        forge.logging.log(data.url);
        
         $scope.$apply(function() {
           setLocalStorage(data.url);
           $location.path('/list');
        });
      });
    };
  };
};

function setLocalStorage(data) {
    localStorage.setItem("userID", getURLParameter('user', data));
    localStorage.setItem("username", getURLParameter('username', data));
    localStorage.setItem("apiKey", getURLParameter('api_key', data));  
};


function ListCtrl($rootScope, $scope, $location, apiCall) {
  function getFoodOptions() {
    console.log('called get');
    var foodList = apiCall.get({
      type: 'food',
      username: localStorage.getItem("username"),
      api_key: localStorage.getItem("apiKey")
    });

    return foodList;
  }

  function getCurrentVote () {
    var currentVote = apiCall.get({
      type: 'vote',
      username: localStorage.getItem("username"),
      api_key: localStorage.getItem("apiKey"),
      user: localStorage.getItem("userID")
    });
  
    return currentVote;
  }

  $scope.food_options = getFoodOptions();
  $scope.current_vote = getCurrentVote();

  $scope.addNew = function() {
    $location.path('/new');
  }

  $scope.attemptVote = function() {
    function sendVote(vote) {
      apiCall.post({
        type: 'vote',
        username: localStorage.getItem("username"),
        api_key: localStorage.getItem("apiKey")
      }, {
        'food_option': {
          'id': vote
        },
        'user': {
          'username': localStorage.getItem("username")
        }
      }, function() {
        $scope.food_options = getFoodOptions();
        $scope.current_vote = getCurrentVote();
      });
    }

    if (typeof $scope.current_vote.objects[0] !== "undefined") {
      if ($scope.current_vote.objects[0].food_option.id === this.food_option.id) {
        apiCall.del({
          type: 'vote',
          username: localStorage.getItem("username"),
          api_key: localStorage.getItem("apiKey"),
          user: localStorage.getItem("userID"),
          id: $scope.current_vote.objects[0].id
        }, function() {
          $scope.food_options = getFoodOptions();
          $scope.current_vote = getCurrentVote();
        });
      }
      else {
        sendVote(this.food_option.id);
      }
    } else {
      sendVote(this.food_option.id);
    }; 
  };
  
  $scope.refresh = function() {
    $scope.food_options = getFoodOptions();
    $scope.current_vote = getCurrentVote();
  };
};

function CreateCtrl($scope, $location, apiCall) {
  $scope.food_options = apiCall.get({
    type: 'food',
    username: localStorage.getItem("username"),
    api_key: localStorage.getItem("apiKey")
  });

  $scope.addOption = function() {
    apiCall.post({
      type: 'food',
      username: localStorage.getItem("username"),
      api_key: localStorage.getItem("apiKey"),
      user: localStorage.getItem("userID")
    }, {
      'name': $scope.optionText,
      'votes': 0
    }, function() {
      $location.path('/list');
    });
  }
}
