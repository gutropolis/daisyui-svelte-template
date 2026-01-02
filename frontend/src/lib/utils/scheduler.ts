
/**
 * Super hacky way to create a scheduler for parallel tasks
 * @param numParallel The number of tasks to run in parallel
 * @param onQueueEmpty This is called whenever the queue becomes empty or the task has been cleared with clear function
 * @param waitDelayMS The number of milliseconds to wait for scheduling the next batch of task
 * @returns 
 */
export function createScheduler(numParallel:number=10, onQueueEmpty?:()=>any, waitDelayMS=100){
  const handlerQueue:(()=>Promise<any>)[] = [];
  let currentCount = 0;
  let isTicking = false;
  
  function onNext(handler: ()=>Promise<any>){
    handlerQueue.push(handler);
    tick();
  }

  async function doNext(){
    try{
      currentCount++;
      await handlerQueue.shift()?.();
    }finally{
      currentCount--;
    }
  }

  async function tick(){
    if(isTicking) return;
    
    isTicking = true;

    while(handlerQueue.length > 0 && isTicking){
      while(currentCount<numParallel && handlerQueue.length > 0 && isTicking){
        doNext();
      }

      // Wait for waitDelayMS before scheduling the next batch of task
      await new Promise(r=>setTimeout(r, waitDelayMS>0?waitDelayMS:100));
    }

    isTicking = false;
    onQueueEmpty?.();
  }

  function clear(){
    // Stop ticking
    isTicking = false;

    // Remove everything from the queue
    handlerQueue.splice(0, Number.MAX_SAFE_INTEGER);
  }

  return { onNext, clear};
}