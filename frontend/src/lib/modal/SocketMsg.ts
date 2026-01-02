/* Copyright (c) 2022. Ankit Patial.
 * Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 * Author: Ankit Patial
 */

import type {SOCKET_ACTION} from "$lib/enums/socket";

export interface SocketMsg<T> {
    action: SOCKET_ACTION;
    data: T;
}
