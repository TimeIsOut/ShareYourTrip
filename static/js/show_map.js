

    ymaps.ready(init);

    function init() {

        var myMap = new ymaps.Map("map", {

            center: [55.76, 37.64],

            zoom: 12,

            controls: [

                'zoomControl',
                'rulerControl',
                'routeButtonControl',
                'trafficControl',
                'typeSelector',
                'fullscreenControl',

                new ymaps.control.SearchControl({
                    options: {
                        size: 'large',
                        provider: 'yandex#search'
                    }
                })

            ]
        });

    }