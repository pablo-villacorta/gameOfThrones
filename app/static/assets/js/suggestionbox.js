let app = new Vue({
    el: "#search-app",
    data: {
        query: "",
        characterResults: [],
        houseResults: [],
        episodeResults: []
    },
    methods: {
        keyup: function() {
            let url = "/api/charactersByName?search="+this.query;
            let self = this;
            self.characterResults = [];
            self.houseResults = [];
            self.episodeResults = [];
            console.log("hey");
            if (this.query.length < 3) return;
            axios
                .get(url)
                .then(function(resp) {
                    self.characterResults = [];
                    for (let i = 0; i < resp.data.length; i++) {
                        let obj = resp.data[i];
                        let toAdd = {
                            id: obj.id,
                            name: obj.name
                        };
                        self.characterResults.push(toAdd);
                    }
                });
            url = "/api/housesByName?search="+this.query;
            axios
                .get(url)
                .then(function(resp) {
                    self.houseResults = [];
                    for (let i = 0; i < resp.data.length; i++) {
                        let obj = resp.data[i];
                        let toAdd = {
                            id: obj.id,
                            name: obj.name
                        };
                        self.houseResults.push(toAdd);
                    }
                });
            url = "/api/episodesByTitle?search="+this.query;
            axios
                .get(url)
                .then(function(resp) {
                    self.episodeResults = [];
                    for (let i = 0; i < resp.data.length; i++) {
                        let obj = resp.data[i];
                        let toAdd = {
                            id: obj.id,
                            name: obj.title
                        };
                        self.episodeResults.push(toAdd);
                    }
                });
        },
        getCharacterUrl: function(n) {
            return "/lore/character/"+n.id;
        },
        getHouseUrl: function(n) {
            return "/lore/house/"+n.id;
        },
        getEpisodeUrl: function(n) {
            return "/lore/episode/"+n.id;
        }
    }
});
