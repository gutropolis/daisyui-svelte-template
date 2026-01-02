export interface EmailTemplate {
    id: string;
    code?: string;
    title?: string;
    subject?: string;
    body?: string;
    smsBody?:string;
    type?:string;
    from?:string;
    token?:string;
} 
export interface EmailTemplateInput {
    id: string;
    code?: string;
    title?: string;
    subject?: string;
    body?: string;
    smsBody?:string;
    type?:string;
    from?:string;
    token?:string;
} 