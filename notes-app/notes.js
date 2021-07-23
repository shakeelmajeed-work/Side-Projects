const fs = require('fs') //Importing the file system module so that we can read and write to the json file (the database)
const chalk = require('chalk')

const addNote = (title,body) => {
    const notes = loadNotes()

    // //need to check if a note with the same title already exists 

    // const duplicate_notes = notes.filter((single_note) => {
    //     //false means that the note is not a duplicate and so it is not saved on this duplicate list of notes

    //     return single_note.title === title 

    //     //condition will return true or false depending on the current title of the iteration and the one inputted by the user
    // })

    const duplicate_note = notes.find((note) => note.title === title) 
    //difference between line above and use of filter above that is that .find stops after finding the first duplicate (does not have to search the rest of the array)

    if (!duplicate_note) { //ie if there are no duplicates 
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

const saveNotes = (notes) => {
    const jsonData = JSON.stringify(notes)
    fs.writeFileSync("database.json",jsonData)
}

const loadNotes = () => {
    try {
        const initial_data = fs.readFileSync("database.json")
        const dataJSON = initial_data.toString()
        return JSON.parse(dataJSON)
    } catch (error) { //code will fail if the file we are trying to write and read from is empty and does not exist 
        return [] //will start an array of JSON Objects 

    }
}


const removeNote = (title) => {
    const notes = loadNotes()

    //2 ways of removing a note. First is to see which object we need to delete from the list of notes and delete it, then save the new list.
    //Other way is to do the inverse and check which notes do not have the required title and save those instead     
    
    
    //using the latter option discussed above 
    //any notes that are 'true' are then saved into this new list of notes 
    const keep_notes = notes.filter((singular_note) => singular_note.title!==title)
    saveNotes(keep_notes)

    
    //Could have just seen if the initial notes list length is bigger than the keep_notes' length to output the appropriate message
    //but opted for this way to increase familiarity with the filter method 
    const removed = notes.filter((singular_note) => singular_note.title===title)

    if (removed.length === 0){
        console.log(chalk.red.inverse("No note has been removed as this note does not exist"))
    } else {
        console.log(chalk.green.inverse("The note with title:",title, " has been removed!"))   
    }
    
}


const listNotes = () => {
    console.log(chalk.blue("Your Notes:"))
    const notes = loadNotes()

    notes.forEach((note) => { //using a method to loop through every note and output its respective title 
        console.log(note.title)
    });


}

const readNote = (title) => {
    notes = loadNotes()
    var indicator = false //a flag to know when we have found a note with the same title 
    for (let i=0; i<notes.length; i++) {
        if (notes[i].title === title) {
            console.log("Title:", chalk.blue.bold(notes[i].title))
            console.log("Body:", notes[i].body)
            indicator = true
        }
    }

    if (!indicator) {
        console.log(chalk.red.inverse("No note with this title has been found!"))
    }

}

module.exports = { //each function from above are objects 
    addNote: addNote,
    removeNote: removeNote,
    listNotes: listNotes,
    readNote: readNote
}