/*
 * jsCalendar language extension
 * Add Nepali Language support
 * Translator: Pravesh Gaire (GairePravesh@github)
 */

// We love anonymous functions
(function(){

    // Get library
    var jsCalendar = window.jsCalendar;

    // If jsCalendar is not loaded
    if (typeof jsCalendar === 'undefined') {
        // If there is no language to load array
        if (typeof window.jsCalendar_language2load === 'undefined') {
            window.jsCalendar_language2load = [];
        }
        // Wrapper to add language to load list
        jsCalendar = {
            addLanguage : function (language) {
                // Add language to load list
                window.jsCalendar_language2load.push(language);
            }
        };
    }

    // Add a new language
    jsCalendar.addLanguage({
        // Language code
        code : 'np',
        // Months of the year
        months : [
            'बैशाख',
            'जेठ',
            'असार',
            'श्रावण',
            'भदौ',
            'आश्विन',
            'कार्तिक',
            'मंसिर',
            'पुष',
            'माघ',
            'फाल्गुन',
            'चैत्र'
        ],
        // Days of the week
        days : [
            'आइतवार',
            'सोमवार',
            'मगलवार',
            'बुधवार',
            'बिहिवार',
            'शुक्रवार',
            'शनिवार'
        ]
    });

})();
