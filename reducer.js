var mongoose = require('mongoose');
var dburl = 'mongodb://localhost:27017/idf-ranking';
mongoose.connect(dburl);
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  console.log('Connected to mongoDB');
});

var heatSchema = mongoose.Schema({
    heatNo: {
        race: String,
        round: Number,
        results: [String]
    }
});
var Heat = mongoose.model('Heat', heatSchema);

Heat.find(function (err, heats) {
  if (err) return console.error(err);
  console.log(heats);
});


var racerSchema = mongoose.Schema({
    racerNo: {
        score: Number,
        beaters: [String],
        losers: [String]
    }
});
var Racer = mongoose.model('Racer', racerSchema);

