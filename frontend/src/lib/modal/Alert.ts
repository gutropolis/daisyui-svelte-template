/* Copyright (c) 2022. Ankit Patial.
 * Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 * Author: Ankit Patial
 */

export default interface Alert {
  id?: number;
  type: "info" | "success" | "warning" | "error";
  title?: string;
  body: string;
  confirmable?: boolean;
  onConfirm?: (data: any) => void;
}
