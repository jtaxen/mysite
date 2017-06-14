/**
 * Created by af on 2017-06-13.
 */

var MYLIBRARY = MYLIBRARY || (function () {
        var _args = {};

        return {
            init : function (Args)  {
                _args = Args;
            },

            helloWorld : function () {
                document.write('Hello ' + _args[0]);
            }
        };
    }());