


// Quesito:
// Date le nuove meccaniche del carosello (si veda video in allegato), scrivere una funzione che consenta di calcolare gli id
// da assegnare alle carte presenti come placeholder, in modo da renderle cliccabili e quindi generare lo spostamento sulla carta desiderata.
// Nota: lo spostamento del carosello è infinito in ambedue le direzioni, ma il numero di carte è finito.
// Per risolvete il quesito bisogna soffermarsi sulla sola funzione.

// Per maggiori informazione vi riporto la storia: https://icbpijira.atlassian.net/browse/DCR-13204



const cards = [0, 1, 2, 3, 4, 5, 6];


const calcPlaceholderId = (arr, id, placeholder) => {

  const placeholderIdStarter = arr.slice(id + 1, id + (placeholder + 1));
  const newIds = arr.slice(0, placeholder);
  let placeholderIdFinal = [];

  if (arr.length > placeholder) {
    placeholderIdFinal = placeholderIdStarter.concat(newIds).slice(0, placeholder);
  } else {
    placeholderIdFinal = placeholderIdStarter.concat(newIds).slice(0, arr.length - 1);
  }

  console.log(placeholderIdFinal);
  return placeholderIdFinal;
}



// calcPlaceholderId(cards, 2, 4);
calcPlaceholderId(cards, 5, 3);


