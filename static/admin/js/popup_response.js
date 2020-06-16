/*
* @Author: Nicolas Flandrois
* @Date:   Thu 11 June 2020 11:44:30
* @Last Modified by:   Nicolas Flandrois
* @Last Modified time: Tue 16 June 2020 14:28:11 
*/
/*global opener */
(function() {
    'use strict';
    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.dismissDeleteRelatedObjectPopup(window, initData.value);
        break;
    default:
        opener.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
        break;
    }
})();
