//-----------------ИНИЦИАЛИЗАЦИЯ_КАРТЫ-------------------//
//-----------------ИНИЦИАЛИЗАЦИЯ_КАРТЫ-------------------//
//-----------------ИНИЦИАЛИЗАЦИЯ_КАРТЫ-------------------//
//-----------------ИНИЦИАЛИЗАЦИЯ_КАРТЫ-------------------//
var mbUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
//-----------------обьявление_интерактивной_и_современной_карты-------------------//

var real = L.tileLayer(mbUrl);
const map = L.map('map', {
    center: [54.757389, 56.041602],
    zoom: 10,
    layers: [real],
    defaultExtentControl: true,
    zoomControl: true,
});
var waypoints=[];
var routingControl=L.Routing.control({
    waypoints:window.waypoints, 
    position: 'topleft',
    routeWhileDragging: false,
    language: 'ru',
    collapsible: true,
    formatter:  new L.Routing.Formatter({
        language: 'ru'}),
    /*onAdd: function (map) 
    {
        // Add reference to map
        map.routingControl= this;
    },*/
    createMarker: function() { icon: L.icon({
            iconUrl: '../static/images/marker-icon.png',
            iconSize: [38, 95],
            iconAnchor: [22, 94],
            popupAnchor: [-3, -76],
            shadowUrl: '../static/images/marker-icon.png',
            shadowSize: [0, 0],
            shadowAnchor: [0, 0]
        })
    },
});
var savedLatLng;
var scale = L.control.scale();
scale.addTo(map);
L.control.locate().addTo(map);

map.on('locationfound', function (evt) {
    savedLatLng = evt.latlng;
    waypoints[0]=savedLatLng;
});

//-----------------ИКОНКИ_И_ПОЛЯ-------------------//
//-----------------ИКОНКИ_И_ПОЛЯ-------------------//
//-----------------ИКОНКИ_И_ПОЛЯ-------------------//
//-----------------ИКОНКИ_И_ПОЛЯ-------------------//
const Icon = L.Icon.extend({
    options: {
        iconSize: [38, 38],
    }
});

const memorialComplexIcon = new Icon({iconUrl: '../static/images/icon1945/MemorialComplexIcon.svg'}),
    eternalFlameIcon = new Icon({iconUrl: '../static/images/icon1945/EternalFlameIcon.svg'}),
    bustIcon = new Icon({iconUrl: '../static/images/icon1945/BustIcon.svg'}),
    steles_oIcon = new Icon({iconUrl: '../static/images/icon1945/Steles_oIcon.svg'}),
    monument_sIcon = new Icon({iconUrl: '../static/images/icon1945/monument_sIcon.svg'}),
    graffitiIcon = new Icon({iconUrl: '../static/images/icon1945/GraffitiIcon.svg'}),
    reliefIcon = new Icon({iconUrl: '../static/images/icon1945/ReliefIcon.svg'}),
    csignIcon = new Icon({iconUrl: '../static/images/icon1945/CsignIcon.svg'}),
    memorialComplexClick = new Icon({iconUrl: '../static/images/icon1945/MemorialComplexIconClick.svg'}),
    eternalFlameClick = new Icon({iconUrl: '../static/images/icon1945/EternalFlameIconClick.svg'}),
    bustClick = new Icon({iconUrl: '../static/images/icon1945/BustIconClick.svg'}),
    steles_oClick = new Icon({iconUrl: '../static/images/icon1945/Steles_oIconClick.svg'}),
    monument_sClick = new Icon({iconUrl: '../static/images/icon1945/Monument_sIconClick.svg'}),
    graffitiClick = new Icon({iconUrl: '../static/images/icon1945/GraffitiIconClick.svg'}),
    reliefClick = new Icon({iconUrl: '../static/images/icon1945/ReliefIconClick.svg'}),
    csignClick = new Icon({iconUrl: '../static/images/icon1945/CsignIconClick.svg'});

var kahim = [" "];
var kahim1 = [" "];
//-----------------СОЗДАНИЕ_ЭКСТЕНТА_КАРТЫ-------------------//
//-----------------СОЗДАНИЕ_ЭКСТЕНТА_КАРТЫ-------------------//
//-----------------СОЗДАНИЕ_ЭКСТЕНТА_КАРТЫ-------------------//
//-----------------СОЗДАНИЕ_ЭКСТЕНТА_КАРТЫ-------------------//
var northWest = L.latLng(55.088755, 55.280588),
southEast = L.latLng(54.299684, 56.791469);
var bounds = L.latLngBounds(northWest, southEast);
map.setMaxBounds(bounds);
map.on('drag', function() {
    map.panInsideBounds(bounds, { animate: false });
});
map.options.minZoom = 10;
//-----------------ЗАГРУЗКА_С_JSON-------------------//
//-----------------ЗАГРУЗКА_С_JSON-------------------//
//-----------------ЗАГРУЗКА_С_JSON-------------------//
//-----------------ЗАГРУЗКА_С_JSON-------------------//

async function load_memorialcomplex(pathpam) {
    const response = await fetch(pathpam)
    const geojson = await response.json()
    return geojson
}

//ждем окончания пред функции
async function render_markers() {

    //-----------------ИКОНКА ЗКАГРУЗКИ САЙТА-------------------//
    
    const memorialcomplex = await load_memorialcomplex('/api/memorialcomplex/');
    const eternalflame = await load_memorialcomplex('/api/eternalflame/');
    const bust = await load_memorialcomplex('/api/bust/');
    const steles_o = await load_memorialcomplex('/api/steles_o/');
    const monument_s = await load_memorialcomplex('/api/monument_s/');
    const graffiti = await load_memorialcomplex('/api/graffiti/');
    const relief = await load_memorialcomplex('/api/relief/');
    const csign = await load_memorialcomplex('/api/csign/');
    const districts = await load_memorialcomplex('/api/districts/');
	var arr1 = [memorialcomplex, eternalflame, bust, steles_o, monument_s, graffiti, relief, csign, districts];

    //-----------------УБРАТЬ ИКОНКУ-------------------//
	return arr1
}

render_markers().then(arr1 => {
    memorialcomplex=arr1[0];
    eternalflame=arr1[1];
    bust=arr1[2];
    steles_o=arr1[3];
    monument_s=arr1[4];
    graffiti=arr1[5];
    relief=arr1[6];
    csign=arr1[7];
    districts=arr1[8];
    
    //-----------------ДАННЫЕ_ДЛЯ_ПОИСКА-------------------//
    //-----------------ДАННЫЕ_ДЛЯ_ПОИСКА-------------------//
    //-----------------ДАННЫЕ_ДЛЯ_ПОИСКА-------------------//
    //-----------------ДАННЫЕ_ДЛЯ_ПОИСКА-------------------//
    ObjectOpts = {
        onEachFeature: function(feature) {
			var p = feature.properties;
			p.index = p.name + " | "; //создаем поле index через которое будем искать по параметрам
            
        },
        //собственные маркеры, которые можно сделать прозрачными
        pointToLayer: function(feature, latlng) {
            return L.marker(latlng, {
                icon: L.divIcon({
                    className: feature.properties.amenity,
                    iconSize: L.point(1, 1),
                    html: feature.properties.amenity[0].toUpperCase(),
                })
            });
        }
    };
    featurelayer = L.layerGroup([ 
		L.geoJson(memorialcomplex, ObjectOpts), //так можно добавлять еще слои в поиск
		L.geoJson(eternalflame, ObjectOpts),
        L.geoJson(bust, ObjectOpts),
        L.geoJson(steles_o, ObjectOpts),
        L.geoJson(monument_s, ObjectOpts),
        L.geoJson(graffiti, ObjectOpts),
        L.geoJson(relief, ObjectOpts),
        L.geoJson(csign, ObjectOpts),
    ]);


    //-----------------СТАНДАРТНЫЕ_ДАННЫЕ-------------------//
    //-----------------СТАНДАРТНЫЕ_ДАННЫЕ-------------------//
    //-----------------СТАНДАРТНЫЕ_ДАННЫЕ-------------------//
    //-----------------СТАНДАРТНЫЕ_ДАННЫЕ-------------------//
    map.on('click', function (e) {
        sidebar.hide();
        chic();
    });
 
        
    var Ufa = L.geoJSON(json_Ufa, {
        style: {
            color: '#ffffff',
            opacity: 0
        },
        onEachFeature: LabelEachFeature
    }).addTo(map);

    var demskiy = L.geoJSON(demskiy_json, {
        style: {
            color: 'blue',
            opacity: 0.5
        },
        onEachFeature: LabelEachFeature
    }).addTo(map);

    var kalininskiy = L.geoJSON(kalininsky_json, {
        style: {
            color: 'red',
            opacity: 0.5
        },
        onEachFeature: LabelEachFeature
    }).addTo(map);

    var kirovskiy = L.geoJSON(kirovskiy_json, {
        style: {
            color: 'green',
            opacity: 0.5
        },
        onEachFeature: LabelEachFeature
    }).addTo(map);

    var leninskiy = L.geoJSON(leninskiy_json, {
        style: {
            color: 'orange',
            opacity: 0.5
        },
        onEachFeature: LabelEachFeature
    }).addTo(map);

    var oktyabrskiy = L.geoJSON(oktyabrskiy_json, {
        style: {
            color: 'purple',
            opacity: 0.5
        },
        onEachFeature: LabelEachFeature
    }).addTo(map);

    var oktyabrskiy2 = L.geoJSON(oktyabrskiy2_json, {
        style: {
            color: 'purple',
            opacity: 0.5
        },
        onEachFeature: LabelEachFeature
    }).addTo(map);

    var ordzhonikidzevskiy = L.geoJSON(ordzhonikidzevskiy_json, {
        style: {
            color: 'brown',
            opacity: 0.5
        },
        onEachFeature: LabelEachFeature
    }).addTo(map);

    var sovetskiy = L.geoJSON(sovetskiy_json, {
        style: {
            color: 'yellow',
            opacity: 0.5
        },
        onEachFeature: LabelEachFeature
    }).addTo(map);

    var MemorialComplexInfo = L.geoJSON(memorialcomplex,{
        onEachFeature: onEachFeatureEternalFlame,
        pointToLayer: ptlMemorialComplex
    }).addTo(map);

    var EternalFlameInfo = L.geoJSON(eternalflame,{
        onEachFeature: onEachFeatureEternalFlame,
        pointToLayer: ptlEternalFlame
    }).addTo(map);

    var BustInfo = L.geoJSON(bust,{
        onEachFeature: onEachFeatureEternalFlame,
        pointToLayer: ptlBust
    }).addTo(map);

    var Steles_oInfo = L.geoJSON(steles_o,{
        onEachFeature: onEachFeatureEternalFlame,
        pointToLayer: ptlSteles_o
    }).addTo(map);

    var Monument_sInfo = L.geoJSON(monument_s,{
        onEachFeature: onEachFeatureEternalFlame,
        pointToLayer: ptlMonument_s
    }).addTo(map);

    var GraffitiInfo = L.geoJSON(graffiti,{
        onEachFeature: onEachFeatureEternalFlame,
        pointToLayer: ptlGraffiti
    }).addTo(map);

    var ReliefInfo = L.geoJSON(relief,{
        onEachFeature: onEachFeatureEternalFlame,
        pointToLayer: ptlRelief
    }).addTo(map);

    var CsignInfo = L.geoJSON(csign,{
        onEachFeature: onEachFeatureEternalFlame,
        pointToLayer: ptlCsign
    }).addTo(map);

    //-----------------КЛАСТЕР-------------------//
    //-----------------КЛАСТЕР-------------------//
    //-----------------КЛАСТЕР-------------------//
    //-----------------КЛАСТЕР-------------------//
    /*const cluster = L.markerClusterGroup();

    cluster.addLayer(MemorialComplexInfo);
    cluster.addLayer(EternalFlameInfo);
    cluster.addLayer(BustInfo);
    cluster.addLayer(Steles_oInfo);
    cluster.addLayer(Monument_sInfo);
    cluster.addLayer(GraffitiInfo);
    cluster.addLayer(ReliefInfo);
    cluster.addLayer(CsignInfo);
    map.addLayer(cluster);*/


    //-----------------ИЗМЕНЕНИЕ_ИКОНКИ-------------------//
    //-----------------ИЗМЕНЕНИЕ_ИКОНКИ-------------------//
    //-----------------ИЗМЕНЕНИЕ_ИКОНКИ-------------------//
    //-----------------ИЗМЕНЕНИЕ_ИКОНКИ-------------------//
    function ptlMemorialComplex(feature,latlng){
        return L.marker(latlng,{icon: memorialComplexIcon}); 
    }

    function ptlEternalFlame(feature,latlng){
        return L.marker(latlng,{icon: eternalFlameIcon}); 
    }

    function ptlBust(feature,latlng){
        return L.marker(latlng,{icon: bustIcon});
    }

    function ptlSteles_o(feature,latlng){
        return L.marker(latlng,{icon: steles_oIcon}); 
    }

    function ptlMonument_s(feature,latlng){
        return L.marker(latlng,{icon: monument_sIcon}); 
    }

    function ptlGraffiti(feature,latlng){
        return L.marker(latlng,{icon: graffitiIcon}); 
    }

    function ptlRelief(feature,latlng){
        return L.marker(latlng,{icon: reliefIcon}); 
    }

    function ptlCsign(feature,latlng){
        return L.marker(latlng,{icon: csignIcon}); 
    }
    //-----------------ОТКРЫТИЕ_ПАНЕЛИ-------------------//
    //-----------------ОТКРЫТИЕ_ПАНЕЛИ-------------------//
    //-----------------ОТКРЫТИЕ_ПАНЕЛИ-------------------//
    //-----------------ОТКРЫТИЕ_ПАНЕЛИ-------------------//
    
    function onEachFeatureEternalFlame(feature, layer) {
        layer.on('click',function(e){
            chic();
            if(e.target.feature.properties.amenity=='Памятник')
            layer.setIcon(monument_sClick);
            else if(e.target.feature.properties.amenity=='ВечныйОгонь')
            layer.setIcon(eternalFlameClick);
            else if(e.target.feature.properties.amenity=='Бюст')
            layer.setIcon(bustClick);  
            else if(e.target.feature.properties.amenity=='Стела')
            layer.setIcon(steles_oClick);  
            else if(e.target.feature.properties.amenity=='ПамятныйЗнак')
            layer.setIcon(csignClick);  
            else if(e.target.feature.properties.amenity=='Рельеф')
            layer.setIcon(reliefClick);  
            else if(e.target.feature.properties.amenity=='Граффити')
            layer.setIcon(graffitiClick);
            else if(e.target.feature.properties.amenity=='МемориальныйКомплекс')
            layer.setIcon(memorialComplexClick);  
            map.flyTo(e.latlng, 17, {
                "animate": true,
                "pan": {
                  "duration": 10000
                }
              });
            openSidebarObject(e);
        });
    }
    
    function LabelEachFeature(feature, layer) {
        layer.on('click',function(e){
            chic();
            //map.setView(e.latlng, 15);
            //openSidebarDistricts(e);
        }),
        map.on('zoomend', function () {
            if (map.getZoom() > 11 && feature.admin_leve!="9") {
                layer.bindTooltip(feature.properties.name, {offset: L.point(0, 0),permanent: true, className: 'AAAA', direction: 'center', setZIndex: 5})
            }
            else if(feature.admin_leve=="9" && map.getZoom() <= 11){
                layer.bindTooltip(feature.properties.name, {offset: L.point(0, 0),permanent: true, className: 'AAAA', direction: 'center', setZIndex: 5})
            }
            else {
                layer.unbindTooltip();
            }
        }),
        console.log(feature.properties);
        map.zoomOut(1);
    }
   
    //------------------БОКОВАЯ_ПАНЕЛЬ------------------//
    //------------------БОКОВАЯ_ПАНЕЛЬ------------------//
    //------------------БОКОВАЯ_ПАНЕЛЬ------------------//
    //------------------БОКОВАЯ_ПАНЕЛЬ------------------//
    
    function openSidebarObject(e) {
        if(sidebar.isVisible()==false){sidebar.show()};
        var popupContentReg=' ';
        kahim1=e.target.feature.properties.photo.split(' ');
        kahimVideo1=e.target.feature.properties.video.split(' ');
        
        
        kahimAudio1=e.target.feature.properties.audio.split(' ');
        photolength=0;
        videolength=0;
        audiolength=0;
        console.log(kahimAudio1); 
        if(kahim1[0]!=""|kahimVideo1[0]!="")
        {
            popupContentReg+='<h3>Галерея фотографий и видео</h3><div>';
            
                photolength=kahim1.length;
                for(var i=0;i<photolength;i++) {
                    if(kahim1[i]!=""){popupContentReg+= '<div class="mySlides fade">\
                    <img src="'+kahim1[i] +'" id="theImage"'+i+'" onClick="makeFullScreen()" class="Image"> </div>';}
                    
                }
                if(kahimVideo1!="")
                videolength=kahimVideo1.length;
            for(var i=0;i<videolength;i++) {
                if(kahimVideo1[i]!=""){popupContentReg+= '<div class="mySlides fade">\
                <video src="'+kahimVideo1[i]+'" controls class="Video"></video></div>';}
                
            }
        
            popupContentReg+='<a class="prev" onclick="plusSlides(-1)">&#10094;</a>\
                            <a class="next" onclick="plusSlides(1)">&#10095;</a>\
                            </div><br>' +'<div style="text-align:center">';

            for(var ii=0;ii<photolength+videolength;ii++)
            {
                popupContentReg+= '<span class="dot" onclick="currentSlide('+(ii+1)+')"></span>';
            }
            popupContentReg+='</div>';
        }
        if(kahimAudio1[0]!=""){
            popupContentReg += '<h3>Аудио-файлы</h3>';
            for (var d = 0; d < kahimAudio1.length; d++) {
                if(kahimAudio1[i]!=""){popupContentReg += '<audio controls><source src="' + kahimAudio1[d] + '" type="audio/mpeg"></audio>';}
                
            }
        }
        /*else if(kahimVideo1!="")
        {
            for(var i=0;i<kahimVideo1.length;i++) {
                popupContentReg+= '<div class="mySlides fade">\
                <video src="'+kahimVideo1[i]+'" controls class="Video"></video></div>';
            }
        }*/
        targeter=e.target;
        materials="";
        if(e.target.feature.properties.amenity!='МемориальныйКомплекс')
        {materials='<p><b>Материал:  </b>' + e.target.feature.properties.material + '<br></p><hr>'}
            sidebar.setContent('<h2>'+ e.target.feature.properties.name + '</h2>' +
            popupContentReg +
            '<p><b>Место:  </b>' + e.target.feature.properties.place + '<br></p><hr>' +
            '<p><b>Дата открытия:  </b>' + e.target.feature.properties.date + '<br></p><hr>'+
            '<p><b>Автор:  </b>' + e.target.feature.properties.author + '<br></p><hr>' +
            '<p><b>Описание:  </b>' + e.target.feature.properties.description + '<br></p><hr>'+
            materials+
            '<p><b>Кто открывал:  </b>' + e.target.feature.properties.who_opened + '<br></p><hr>'+
            '<p><b>Территория вокруг:  </b>' + e.target.feature.properties.area_around + '<br></p><hr>'+
            '<p><b>Уровень охраны:  </b>' + e.target.feature.properties.security_level + '<br></p><hr>'+
            '<p><b>Привязан к конкретной местности или просто памятник (место рождения героя, место формирования полка):  </b>' + 
            e.target.feature.properties.binding + '<br></p>'+ 
            '<button class="routeButton" onClick="marshend(targeter)">Построить маршрут</button><br>');
            showSlides();
        //sidebar.setContent(sidebar+'<br><button>Текст</button>' );   
    }

    function openSidebarDistricts(e) {
        if(sidebar.isVisible()==false){sidebar.show()};
        var popupContentReg=' ';
        //-----------------ДОБАВИТЬ_МЕДИА?-------------------//
        sidebar.setContent('<h1>'+ e.target.feature.properties.name + '</h1>' +
        '<p>Мемориальные комплексы (' + e.target.feature.properties.memorialcomplex_set + '): ' + e.target.feature.properties.memorialcomplex_set +
        '<p>Вечные огни (' + e.target.feature.properties.eternalflame_set + '): ' + e.target.feature.properties.eternalflame_set +
        '<p>Бюсты (' + e.target.feature.properties.bust_set + '): ' + e.target.feature.properties.bust_set +
        '<p>Стелы (обелиски) (' + e.target.feature.properties.steles_o_set + '): ' + e.target.feature.properties.steles_o_set +
        '<p>Памятники (скульптуры) (' + e.target.feature.properties.monument_s_set + '): ' + e.target.feature.properties.monument_s_set +
        '<p>Граффити (' + e.target.feature.properties.graffiti_set + '): ' + e.target.feature.properties.graffiti_set +
        '<p>Рельефы (' + e.target.feature.properties.relief_set + '): ' + e.target.feature.properties.relief_set +
        '<p>Памятные знаки (' + e.target.feature.properties.csign_set + '): ' + e.target.feature.properties.csign_set);
        showSlides();
    }
    

    
        //-----------------ФИЛЬТР-------------------//
        //-----------------ФИЛЬТР-------------------//
        //-----------------ФИЛЬТР-------------------//
        //-----------------ФИЛЬТР-------------------//
    var baseTree = {
        label: 'Карта',

        children: [
            {
                label: ' Город Уфа', layer: real
            },
          ]
    };
        
    var overlaysTree = {
        label: 'Слои',
        children: [{
            label: 'Районы города Уфа',
            selectAllCheckbox: true,
            collapsed: true,
            children: [
                {
                    label: ' Дёмский район', layer: demskiy,
                },
                {
                    label: ' Калининский район', layer: kalininskiy,
                },
                {
                    label: ' Кировский район', layer: kirovskiy,
                },
                {
                    label: ' Ленинский район', layer: leninskiy,
                },
                {
                    label: ' Октябрьский район (город)', layer: oktyabrskiy
                },
                {
                    label: ' Октябрьский район (за городом)', layer: oktyabrskiy2
                },
                {
                    label: ' Орджоникидзевский район', layer: ordzhonikidzevskiy,
                },
                {
                    label: ' Советский район', layer: sovetskiy,
                },
            ]
        },
        {
            label: 'Объекты',
            selectAllCheckbox: true,
            children: [
                {
                    label: '<img src="../static/images/icon1945/MemorialComplexIcon.svg" class="imgtree"> Мемориальные комплексы', layer: MemorialComplexInfo,
                },
                {
                    label: '<img src="../static/images/icon1945/EternalFlameIcon.svg" class="imgtree"> Вечные огни', layer: EternalFlameInfo,
                },
                {
                    label: '<img src="../static/images/icon1945/BustIcon.svg" class="imgtree"> Бюсты', layer: BustInfo,
                },
                {
                    label: '<img src="../static/images/icon1945/Steles_oIcon.svg" class="imgtree"> Стелы (обелиски)', layer: Steles_oInfo,
                },
                {
                    label: '<img src="../static/images/icon1945/Monument_sIcon.svg" class="imgtree"> Памятники (скульптуры)', layer: Monument_sInfo,
                },
                {
                    label: '<img src="../static/images/icon1945/GraffitiIcon.svg" class="imgtree"> Граффити', layer: GraffitiInfo,
                },
                {
                    label: '<img src="../static/images/icon1945/ReliefIcon.svg" class="imgtree"> Рельефы', layer: ReliefInfo,
                },
                {
                    label: '<img src="../static/images/icon1945/CsignIcon.svg" class="imgtree"> Памятные знаки', layer: CsignInfo,
                },
            ]
        }
    ]
    };

    var lay = L.control.layers.tree(baseTree, overlaysTree,
        {
            namedToggle: false,
            selectorBack: false,
            collapseAll: 'Свернуть все',
            expandAll: 'Раскрыть все',
            collapsed: true,
        });
    lay.addTo(map);

    //-----------------ЛЕГЕНДА-------------------//
    //-----------------ЛЕГЕНДА-------------------//
    //-----------------ЛЕГЕНДА-------------------//
    //-----------------ЛЕГЕНДА-------------------//
    L.control.Legend({
        position: "bottomright",
        title: "Легенда",
        column: 2,
        legends: [
            {
                label: "Мемориальный комплекс",
                type: "image",
                url: "../static/images/icon1945/MemorialComplexIcon.svg",
            },
            {
                label: "Вечный огонь",
                type: "image",
                url: "../static/images/icon1945/EternalFlameIcon.svg",
            },
            {
                label: "Бюст",
                type: "image",
                url: "../static/images/icon1945/BustIcon.svg",
            },
            {
                label: "Стела (обелиск)",
                type: "image",
                url: "../static/images/icon1945/Steles_oIcon.svg",
            },
            {
                label: "Памятник (скульптура)",
                type: "image",
                url: "../static/images/icon1945/Monument_sIcon.svg",
            },
            {
                label: "Граффити",
                type: "image",
                url: "../static/images/icon1945/GraffitiIcon.svg",
            },
            {
                label: "Рельеф",
                type: "image",
                url: "../static/images/icon1945/ReliefIcon.svg",
            },
            {
                label: "Памятный знак",
                type: "image",
                url: "../static/images/icon1945/CsignIcon.svg",
            },
            {
                label: "Дёмский район",
                type: "image",
                url: "../static/images/icon1945/demskiy.svg",
            },
            {
                label: "Калининский район",
                type: "image",
                url: "../static/images/icon1945/kalininskiy.svg",
            },
            {
                label: "Кировский район",
                type: "image",
                url: "../static/images/icon1945/kirovskiy.svg",
            },
            {
                label: "Ленинский район",
                type: "image",
                url: "../static/images/icon1945/leninskiy.svg",
            },
            {
                label: "Октябрьский район",
                type: "image",
                url: "../static/images/icon1945/oktyabrskiy.svg",
            },
            {
                label: "Орджоникидзевский район",
                type: "image",
                url: "../static/images/icon1945/ordzhonikidzevskiy.svg",
            },
            {
                label: "Советский район",
                type: "image",
                url: "../static/images/icon1945/sovetskiy.svg",
            },

        ]
    }).addTo(map);

    
        
    //-----------------ПОИСК-------------------//
    //-----------------ПОИСК-------------------//
    //-----------------ПОИСК-------------------//
    //-----------------ПОИСК-------------------//
    var controlSearch = new L.Control.Search({	
		layer: featurelayer,
		initial: false, // не обязательно вводить слово в слово при false
		propertyName: 'index',
		zoom: 17,
		marker: false,
		buildTip: function(text, val) {
			var type = val.layer.feature.properties.amenity; // будет указываться что за тип ищется
            var engltype = val.layer.feature.properties.amenity1; // будет настройка стиля для искомого типа
			return '<a href="#" class="'+engltype+'">'+text+'<b>'+type+'</b></a>';
		}
	});
	// открываем балун, если нашли
	controlSearch.on('search:locationfound', function(e) {  
        //-----------------ОТКРЫТИЕ БАЛУНА ПРИ НАХОЖДЕНИИ-------------------//
        e.layer.openpopup();
	})
	map.addControl( controlSearch );
    });