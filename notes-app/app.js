const chalk = require('chalk')
const notes = require('./notes.js')
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
    handler(argv) {
        notes.addNote(argv.title,argv.body)

    }
})


//Create  remove command for notes app 

yargs.command({
    command: 'remove',
    describe: "Remove a note",
    builder: {
        title: {
            describe: 'Remove a note',
            demandOption: true,
            type: 'string'
        }
    },
    handler(argv) {
        notes.removeNote(argv.title)
    }
})

//Create list command for notes app 

yargs.command({
    command: 'list',
    describe: "List all notes ",
    handler() {
        console.log("Showing all notes")
    }
})

//Create read command for notes app

yargs.command({
    command: 'read',
    describe: "Read a note",
    handler() {
        console.log("Outputting the note!")
    }
})

yargs.parse()
