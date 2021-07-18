const chalk = require('chalk')
const getNotes = require('./notes.js')
const yargs = require('yargs')


// Create add command for notes app 

yargs.command({
    command: 'add',
    describe: "Add a new note",
    builder: {
        title: {
            describe: 'Title of your note',
            demandOption: true, //Ensures that this is always required
            type: 'string' //Ensures we do not get boolean or any other data type as our title 
        },
        body: {
            describe: "Input a body to your note",
            demandOption: true,
            type: 'string'
        }
    },
    handler: function (argv) {
        console.log("Title: ",argv.title)
        console.log("Body: ", argv.body)

    }
})


//Create  remove command for notes app 

yargs.command({
    command: 'remove',
    describe: "Remove a note",
    handler: function () {
        console.log("Removing the note!")
    }
})

//Create list command for notes app 

yargs.command({
    command: 'list',
    describe: "List all notes ",
    handler: function () {
        console.log("Showing all notes")
    }
})

//Create read command for notes app

yargs.command({
    command: 'read',
    describe: "Read a note",
    handler: function () {
        console.log("Outputting the note!")
    }
})

yargs.parse()

// const command = process.argv[2]

// if (command === "add") { 
//     console.log("Going to add note")
// } else if (command === "remove") {
//     console.log("Removing note")
// }