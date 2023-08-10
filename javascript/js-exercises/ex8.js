/*
function tests(){
    return new Promise(function(resolve,reject)){
        const error = false;
        if(error){
            reject('Error...');
        }else{
            resolve("Promise was succesfully solved!");
        }
    }
}

tests().then(function(res){
    alert(res);
}).catch(function(err)){
    alert(err);
}
*/ //Promise

function tests(){
    return new Promise(function(resolve,reject)){
        setTimeout(function(){
            const error = false;
            if(error){
                reject('Error...');
            }else{
                resolve("Promise was succesfully solved!");
            }
        },2000)
    }
}

async function tests2(){
    await tests2().then(function(res){
        alert(res);
    });
    alert('hello!');
} 

tests2();

//use of await in asyncronows functions(just execute hello when the promise is resolved)

var p = document.getElementsByTagName('p');

for(var i = 0; i < 10; i ++){
    p[0].innerHTML = p[0].innerHTML + "- algo -";
}

for(var k = 1; k < p.length; k ++){
    p[k].innerHTML = 'Manipulado via JS!' + k;
}