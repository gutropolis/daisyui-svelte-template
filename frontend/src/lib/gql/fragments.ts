import { gql } from "@urql/svelte";

export const user = gql`
    fragment user on User {
        id
        email
        name
        firstName
        middleName
        lastName
        phone
        picture
        role
        status
    }
`;
export const session = gql`
    fragment session on User {
        id
        email
        name
        picture
        role
    }
`;

export const connector = gql`
    fragment connector on Connector {
        id
				type
        name
        apiUrl
        apiUser 
        apiSecretMask
        description
        creator {
            id
            name
        }
    }
`;
export const chiefInvestigator = gql`
    fragment chiefInvestigator on ProjectUser {
        id
        userId
        name
        role{
            name 
            title 
            id
        }
    }
`;

export const projectUser = gql`
    fragment projectUser on ProjectUser {
        id,
        name,
        
        userId,
        role{
            id,
            name,
            title
        }
        user{
            id,
            name,
            email,
            phone, 
        },
        site{
            id
            name
             
        } 
    }
`;
export const projectTimeline = gql`
    fragment projectModality on ProjectModality{
        id,
        title, 
        modality, 
    }
`;

export const project = gql`
    fragment project on Project {
        id
        code
        clientName
        clientContact
        name 
        startAt
        endAt 
        activeSites
        setting{
            maxSites
            maxSubjects
            isSelfReviewAllowed
            performDeIdentification
        }
        totalSubjects
        bodyPart
        description
        diseaseArea
        licence 
        status
    }
`;
export const myProject = gql`
    fragment myProject on Project {
        id
        clientName
        clientContact
        name 
        startAt
        endAt 
        role
        activeSites
        code
        setting{
            maxSites
            maxSubjects
            isSelfReviewAllowed
            performDeIdentification
        } 
        totalSubjects
        description
        userSiteId
        bodyPart
        licence
        diseaseArea
        status
				
    }
`;
export const site = gql`
    fragment site on ProjectSite {
        id,
        name,
        address,
        code,
        primaryContact,
    }
`;

export const subject = gql`
    fragment subject on Subject {
        id
        firstName
        lastName
        sex
        age
        dateEnrolled
        admissionDate
        dob
        extraField
        code 
        customID
        project{
            id
        }
        site{
            id
            name 
            address 
            code
        }
         
        timepoints{
            id, 
            form{
                id
                name
                scanType 
                seriesType 
            }
						event{
								title
								description
								name
								id
						}
            status
            modality 
        } 
    }
`;

export const study = gql`
    fragment study on Study {
        id
        uid
        patientName
        patientAge
        patientSex
        date
        time
        accessionNum
        modality 
        totalInstances 
        project{
        name
        }
        site {
            name     
        }
    }
`;

export const imgSeries = gql`
    fragment imgSeries on Series {
        id
        uid
        number
        description
        modality
        totalInstances
        status
		reason
		totalInvalidInstances 		
    }
`;
export const series = gql`
    fragment series on Series {
        id
        uid
        number
        description
        modality
        totalInstances
        status
		reason
		totalInvalidInstances
				
				
    }
`;

export const log = gql`
    fragment  log on AuditLog {
        id
        user{
            id,
            name
        }
        action
        description
        ip
    }
`;


export const formfield = gql`
    fragment formfield on  FormField {
        id
        type
        label
        name
        placeholder
        description
        validate
        defaultValue
        attribute {
            cssClass
            multiple
            hasOptions
            format
            options {
                id
                name
            }
            validation,
            conditions {
                state
                conditionType
                conditions {
                    field
                    hasOptions
                    id
                    operator
                    options {
                        id
                        name
                    }
                    value
                    whereOperator
                    __typename
                }
            }
        }
        active
        order

    }
`;


export const subjTimePoint  = gql`
    fragment subjTimePoint on SubjectTimePoint {
        id
        title
        modality
        status
        imagingStatus
        creator{
            name
        }
        project{
            id
        }
        subject{
            id
            firstName
            lastName
            sex
            dateEnrolled
            admissionDate
            dob
            extraField
            code
            site{
                id
            }
        }
        form{
            id
            name
            description
            title 
        },
        site{
            id
        }
        event{
            title
            name
            id
            description
        }
        eventStatus{
            status
        }
        reason
        studyCount
    }
`;

export const projectgroups = gql`
    fragment projectgroups on ProjectGroups {
        modalities{
            id
            name
            title
            order
            scanType
            seriesType
        }
        clinicals{
            id,
            name
            title
            order
        }
    }
`;

export const projectEvent = gql`
    fragment projectEvent on ProjectEvent{
        id,
        name,
        title,
        description,
    }
`;