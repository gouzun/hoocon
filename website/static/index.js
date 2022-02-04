function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function wnamedropdownSelected(){
  let workernamedropdown = document.forms["myForm"]['workernamedropdown'].value;
  
  if (workernamedropdown != "Select worker name here"){   
    wname = workernamedropdown;    
    document.getElementById('wname').value = wname;
  }
  else {    
    document.getElementById('wname').value = "";    
  }
  
}

function salarydatedropdownSelected(){
  const d = new Date();
  let month = d.getMonth();
  let year = d.getFullYear();
  
  let salarydatedropdown = document.forms["myForm"]['salarydatedropdown'].value;
  
  if (salarydatedropdown != "Select month/year here"){   
    document.getElementById('salarydate').value = salarydatedropdown;
  }
  else {
    month = month -1;
    if (month==-1){
      month = 12;
      year = year - 1;
    } else{      
      month = month + 2;
    }    
    document.getElementById('salarydate').value = month +"-"+year;    
  }
  
}

function projectdropdownSelected(){

  let projectdropdown = document.forms["myForm"]['projectdropdown'].value;
  
  if (projectdropdown != "Select project title here"){   
    projectlocation = projectdropdown;    
    document.getElementById('projectlocation').value = projectlocation;    
  }
  else {    
    document.getElementById('projectlocation').value = "";    
  }
  
}
 
function validateForm(form) {
  
  let workernamedropdown = form.workernamedropdown.value;           
  let projectdropdown = document.forms["myForm"]['projectdropdown'].value;
  let wname = document.forms["myForm"]["wname"].value;
  let projectlocation = document.forms["myForm"]["projectlocation"].value;
  let dayrate = document.forms["myForm"]["dayrate"].value;

  /*to validate worker name*/    
  if (workernamedropdown=="Select worker name here"){    
    if (wname == "") {      
      alert("Please key in or select worker name.");
      document.getElementById('wname').focus();
      return false;
    }        
  }
  /*end - to validate worker name */

  /*to validate project tittle */
  if (projectdropdown=="Select project title here"){
    if (projectlocation == "") {
      alert("Please key in or select a project name.");
      document.getElementById('projectlocation').focus();
      return false;
    }       
  }
  
  if (dayrate == "" || dayrate == 0) {
    alert("Please key in worker day rate");
    document.getElementById('dayrate').focus();
    return false;
  }

}

function validateFormSearch(form) {

  let workernamedropdown = document.forms["myForm"]['searchworkernamedropdown'].value;           
  let projectdropdown = document.forms["myForm"]['searchprojectdropdown'].value;
  let wname = document.forms["myForm"]["searchwname"].value;
  let projectlocation = document.forms["myForm"]["searchprojectlocation"].value;
  let salarydatedropdown = document.forms["myForm"]["searchsalarydatedropdown"].value;
  let salarydate = document.forms["myForm"]["searchsalarydate"].value;

  /*to validate worker name*/  
  if (workernamedropdown=="Select worker name here"){
    if (wname == ""){
      alert("Please key in or select a worker name.");
      document.getElementById('searchwname').focus();
      return false;
    }    
  }
  /*end - to validate worker name */

  /*to validate project tittle */
  if (projectdropdown=="Select project title here"){ 
    if (projectlocation == "") {
      alert("Please key in or select a project name.");
      document.getElementById('searchprojectlocation').focus();
      return false;
    }       
  }
/* end - to validate project tittle */
  if (salarydatedropdown=="Select month/year here"){  
    if (salarydate == "") {
      alert("Please key in or select a psalary month.");
      document.getElementById('searchsalarydate').focus();
      return false;
    }       
  }
}

function setpreviousmonth(){  
  const d = new Date();
  let month = d.getMonth();
  let year = d.getFullYear();
 
  month = month -1;
  if (month==-1){
      month = 12;
      year = year - 1;      
    }
    else {
      month = month + 1;
          
  }
  document.getElementById('salarydate').value = month +"-"+year;  //for input_salary.html  
}

function searchwnamedropdownSelected(){
  let workernamedropdown = document.forms["myForm"]['searchworkernamedropdown'].value;
  
  if (workernamedropdown != "Select worker name here"){   
    wname = workernamedropdown;    
    document.getElementById('searchwname').value = wname;
  }
  else {    
    document.getElementById('searchwname').value = "";    
  }
  
}

function searchsalarydatedropdownSelected(){
  const d = new Date();
  let month = d.getMonth();
  let year = d.getFullYear();
  
  let salarydatedropdown = document.forms["myForm"]['searchsalarydatedropdown'].value;
  
  if (salarydatedropdown != "Select month/year here"){   
    document.getElementById('searchsalarydate').value = salarydatedropdown;
  }
  else {
    month = month -1;
    if (month==-1){
      month = 12;
      year = year - 1;
    } else{      
      month = month + 2;
    }    
    document.getElementById('searchsalarydate').value = month +"-"+year;    
  }
  
}

function searchprojectdropdownSelected(){

  let projectdropdown = document.forms["myForm"]['searchprojectdropdown'].value;
  
  if (projectdropdown != "Select project title here"){   
    projectlocation = projectdropdown;    
    document.getElementById('searchprojectlocation').value = projectlocation;    
  }
  else {    
    document.getElementById('searchprojectlocation').value = "";    
  }  
}