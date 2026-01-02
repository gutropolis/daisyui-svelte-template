/**
 * @param test the value to clamp
 * @param start lower limit
 * @param end upper limit
 * @returns value in range [start, end]
 */
export function clamp(test:number, start:number, end: number):number{
  if(test<start) return start;
  if(test>end) return end;
  return test;
}