/*
* @Author: Nicolas Flandrois
* @Date:   Thu 11 June 2020 11:44:30
* @Last Modified by:   Nicolas Flandrois
* @Last Modified time: Tue 16 June 2020 14:28:10 
*/
(function($) {
    'use strict';
    $(function() {
        $('.cancel-link').on('click', function(e) {
            e.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
                window.history.back(); // Go back if not a popup.
            } else {
                window.close(); // Otherwise, close the popup.
            }
        });
    });
})(django.jQuery);
