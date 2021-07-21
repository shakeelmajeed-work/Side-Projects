const fs = require('fs') //Importing the file system module so that we can read and write to the json file (the database)
const chalk = require('chalk')


const getNotes = function () {
    return 'Your notes...'
}

const addNote = function(title,body) {
    const notes = loadNotes()

    //need to check if a note with the same title already exists 
    const duplicate_notes = notes.filter(function (single_note) {
        //false means that the note is not a duplicate and so it is not saved on this duplicate list of notes
        
        return single_note.title === title 
        //condition will return true or false depending on the current title of the iteration and the //one inputted by the user

    })

    if (duplicate_notes.length === 0) { //ie if there are no duplicates 
        notes.push({ //using parameters passed in to define what note and its attributes will be appended to the database
            title: title,
            body: body
        })
        saveNotes(notes) //after loading it in and editing the list of notes, calling helper function to save it   
        console.log(chalk.green.inverse("Note has been added"))
    } else {
        console.log(chalk.red.inverse("Note with the same title already exists!"))
    }

}

const saveNotes = function(notes) {
    const jsonData = JSON.stringify(notes)
    fs.writeFileSync("database.json",jsonData)
}

const loadNotes = function() {
    try {
        const initial_data = fs.readFileSync("database.json")
        const dataJSON = initial_data.toString()
        return JSON.parse(dataJSON)
    } catch (error) { //code will fail if the file we are trying to write and read from is empty and does not exist 
        return [] //will start an array of JSON Objects 

    }
}


module.exports = {
    getNotes: getNotes,
    addNote: addNote 
}